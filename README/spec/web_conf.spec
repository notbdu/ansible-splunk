############################################
#
# Possible values for conf/web role
#
# Follows Splunk web.conf.spec closely
#
############################################

splunk_web_conf:
  settings:
    enableSplunkWebSSL: [True | False]
    * Defaults to True

    httpport: <port>
    * Defaults to 8000

    startwebserver: [True | False]
    * Defaults to True

    privKeyPath: <path>
    * Relative paths are interpreted as relative to $SPLUNK_HOME
    * Defaults to etc/auth/splunkweb/privkey.pem

    caCertPath:  <path>
    * Relative paths are interpreted as relative to $SPLUNK_HOME
    * Default to etc/auth/splunkweb/cert.pem

    updateCheckerBaseURL: [http://quickdraw.Splunk.com/js/|0]
    * Defaults to http://quickdraw.Splunk.com/js/

    trustedIP: 127.0.0.1
    * For SSO, reverse proxy.  Allow localhost to talk to Splunk

    SSOMode: strict
    * For SSO, see Splunk documentation for details

    remoteUser: Cas-User
    * CASAuthNHeader, use Cas-User as this is what is hard-coded in the
      included httpd/Apache vhost template file.
