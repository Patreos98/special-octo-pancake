/**
 * @fileoverview Rule to require sorting of variables within a single Variable Declaration block
 * @author Ilya Volodin
 */

"use strict";

//------------------------------------------------------------------------------
// Rule Definition
//------------------------------------------------------------------------------

module.exports = {
    meta: {
        docs: {
            description: "require variables within the same declaration block to be sorted",
            category: "Stylistic Issues",
            recommended: false
        },

        schema: [
            {
                type: "object",
                properties: {
                    ignoreCase: {
                        type: "boolean"
                    }
                },
                additionalProperties: false
            }
        ],

        fixable: "code"
    },

    create(context) {

        const configuration = context.options[0] || {},
            ignoreCase = configuration.ignoreCase || false,
            sourceCode = context.getSourceCode();

        return {
            VariableDeclaration(node) {
                const idDeclarations = node.declarations.filter(decl => decl.id.type === "Identifier");
                const getSortableName = ignoreCase ? decl => decl.id.name.toLowerCase() : decl => decl.id.name;
                const unfixable = idDeclarations.some(decl => decl.init !== null && decl.init.type !== "Literal");
                let fixed = false;

                idDeclarations.slice(1).reduce((memo, decl) => {
                    const lastVariableName = getSortableName(memo),
                        currentVariableName = getSortableName(decl);

                    if (currentVariableName < lastVariableName) {
                        context.report({
                            node: decl,
                            message: "Variables within the same declaration block should be sorted alphabetically.",
                            fix(fixer) {
                                if (unfixable || fixed) {
                                    return null;
                                }
                                return fixer.replaceTextRange(
                                    [idDeclarations[0].range[0], idDeclarations[idDeclarations.length - 1].range[1]],
                                    idDeclarations

                                        // Clone the idDeclarations array to avoid mutating it
                                        .slice()

                                        // Sort the array into the desired order
                                        .sort((declA, declB) => {
                                            const aName = getSortableName(declA);
                                            const bName = getSortableName(declB);

                                            return aName > bName ? 1 : -1;
                                        })

                                        // Build a string out of the sorted list of identifier declarations and the text between the originals
                                        .reduce((sourceText, identifier, index) => {
                                            const textAfterIdentifier = index === idDeclarations.length - 1
                                                ? ""
                                                : sourceCode.getText().slice(idDeclarations[index].range[1], idDeclarations[index + 1].range[0]);

                                            return sourceText + sourceCode.getText(identifier) + textAfterIdentifier;
                                        }, "")

                                );
                            }
                        });
                        fixed = true;
                        return memo;
                    }
                    return decl;

                }, idDeclarations[0]);
            }
        };
    }
};
