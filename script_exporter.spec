Name:           script_exporter
Version:        1.2
Release:        1%{?dist}
Summary:        script_exporter service for running script_exporter

License:        GPLv3
URL:            https://github.com/ricoberger/script_exporter
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

%description
Prometheus exporter to execute scripts and collect metrics from the output or the exit status. - This is only working in Combination with Grafana Alloy! :)

%prep
# This section is left empty since we're not patching or preparing sources.


%build
# No build required as we are just packaging a binary.

%install
# Create directories if needed
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/etc/sysconfig
# Install the binary
install -m 755 %{_sourcedir}/script_exporter %{buildroot}/usr/bin/script_exporter

# Install the systemd service file
install -m 644 %{_sourcedir}/script_exporter.service %{buildroot}/usr/lib/systemd/system/script_exporter.service

# Install the sysconfig file
install -m 644 %{_sourcedir}/script_exporter.config %{buildroot}/etc/sysconfig/script_exporter.config

%pre
# Actions before installing/upgrading the new package
# For an update, stop the running service before we install the new version
# This script runs before installation to check if the user exists, and creates it if necessary.
# Create a new system user "myappuser" if it doesn't already exist
getent passwd alloy > /dev/null 2>&1 || useradd -r -s /sbin/nologin -M alloy

if [ $1 -gt 1 ]; then
    systemctl stop script_exporter.service || true
fi


%post
# Actions after installing/upgrading the new package
# For an upgrade or installation, ensure the service is enabled and restarted
if [ $1 -eq 1 ]; then
    systemctl enable script_exporter.service || true
fi
systemctl daemon-reload
# Restart the service only during update or downgrade ($1 == 2)
if [ $1 -eq 2 ]; then
    systemctl restart myapp.service || true
fi

%preun
# Actions before uninstalling or upgrading the old package
# During uninstallation or an update, stop the service before removing the old package
if [ $1 -eq 0 ]; then
    systemctl stop script_exporter.service || true
    systemctl disable script_exporter.service || true
fi

%postun
# Actions after uninstalling or downgrading the old package
# If this is not an upgrade, reload systemd to clear any references to the old service
if [ $1 -ge 1 ]; then
    systemctl daemon-reload
fi

%files
/usr/bin/script_exporter
/usr/lib/systemd/system/script_exporter.service
/etc/sysconfig/script_exporter.config

%changelog
* Sat Sep 07 2024 Julian Kirstein <julian.kirstein@de.markant.com> - 1.2-1
- Initial package