{
  'variables': {
    'openssl_defines_linux-ppc64le': [
      'NDEBUG',
      'OPENSSL_USE_NODELETE',
      'L_ENDIAN',
      'OPENSSL_PIC',
      'OPENSSL_CPUID_OBJ',
      'OPENSSL_BN_ASM_MONT',
      'SHA1_ASM',
      'SHA256_ASM',
      'SHA512_ASM',
      'KECCAK1600_ASM',
      'AES_ASM',
      'VPAES_ASM',
      'ECP_NISTZ256_ASM',
      'X25519_ASM',
      'POLY1305_ASM',
    ],
    'openssl_cflags_linux-ppc64le': [
      '-Wa,--noexecstack',
      '-Wall -O3',
      '-pthread -m64',
      '-Wall -O3',
    ],
    'openssl_ex_libs_linux-ppc64le': [
      '-ldl -pthread',
    ],
    'openssl_cli_srcs_linux-ppc64le': [
      'openssl/apps/asn1pars.c',
      'openssl/apps/ca.c',
      'openssl/apps/ciphers.c',
      'openssl/apps/cms.c',
      'openssl/apps/crl.c',
      'openssl/apps/crl2p7.c',
      'openssl/apps/dgst.c',
      'openssl/apps/dhparam.c',
      'openssl/apps/dsa.c',
      'openssl/apps/dsaparam.c',
      'openssl/apps/ec.c',
      'openssl/apps/ecparam.c',
      'openssl/apps/enc.c',
      'openssl/apps/engine.c',
      'openssl/apps/errstr.c',
      'openssl/apps/gendsa.c',
      'openssl/apps/genpkey.c',
      'openssl/apps/genrsa.c',
      'openssl/apps/nseq.c',
      'openssl/apps/ocsp.c',
      'openssl/apps/openssl.c',
      'openssl/apps/passwd.c',
      'openssl/apps/pkcs12.c',
      'openssl/apps/pkcs7.c',
      'openssl/apps/pkcs8.c',
      'openssl/apps/pkey.c',
      'openssl/apps/pkeyparam.c',
      'openssl/apps/pkeyutl.c',
      'openssl/apps/prime.c',
      'openssl/apps/rand.c',
      'openssl/apps/rehash.c',
      'openssl/apps/req.c',
      'openssl/apps/rsa.c',
      'openssl/apps/rsautl.c',
      'openssl/apps/s_client.c',
      'openssl/apps/s_server.c',
      'openssl/apps/s_time.c',
      'openssl/apps/sess_id.c',
      'openssl/apps/smime.c',
      'openssl/apps/speed.c',
      'openssl/apps/spkac.c',
      'openssl/apps/srp.c',
      'openssl/apps/storeutl.c',
      'openssl/apps/ts.c',
      'openssl/apps/verify.c',
      'openssl/apps/version.c',
      'openssl/apps/x509.c',
      'openssl/apps/app_rand.c',
      'openssl/apps/apps.c',
      'openssl/apps/bf_prefix.c',
      'openssl/apps/opt.c',
      'openssl/apps/s_cb.c',
      'openssl/apps/s_socket.c',
    ],
  },
  'defines': ['<@(openssl_defines_linux-ppc64le)'],
  'include_dirs': [
    './include',
  ],
  'cflags' : ['<@(openssl_cflags_linux-ppc64le)'],
  'libraries': ['<@(openssl_ex_libs_linux-ppc64le)'],
  'sources': ['<@(openssl_cli_srcs_linux-ppc64le)'],
}
