# rpm-build-script-exporter
rpm_build example is the script-exporter

### needed linux packages:
rpm-build
### nice to have:
rpmdevtools #builds the Tree needed under home

##How to do it
### inital
- build the rpmbuild Tree to home
rpmdev-setuptree
- build the source files to a tarball
tar czf ~/rpmbuild/SOURCE/name-version.tar.gz sourcefile1 sourcefile2
- setup and cp the spec file:
vi speccname.spec
cp speccname.spec ~/rpmbuild/SPECS/
- build the rpm
rpmbuild -ba ~/rpmbuild/SPECS/speccname.spec
