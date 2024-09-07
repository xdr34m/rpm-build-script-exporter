# rpm-build-script-exporter
rpm_build example is the script-exporter

### needed linux packages:
rpm-build
### nice to have:
rpmdevtools #builds the Tree needed under home

## How to do it
### inital
- build the rpmbuild Tree to home<br>
rpmdev-setuptree

### for everybuild
- build the source files to a tarball<br>
tar czf ~/rpmbuild/SOURCE/name-version.tar.gz sourcefile1 sourcefile2
- setup and cp the spec file:<br>
vi speccname.spec<br>
cp speccname.spec ~/rpmbuild/SPECS/
- build the rpm<br>
rpmbuild -ba ~/rpmbuild/SPECS/speccname.spec
