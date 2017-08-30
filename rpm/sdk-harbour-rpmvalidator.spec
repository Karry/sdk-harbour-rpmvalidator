%global __python %{__python3}

Name:       sdk-harbour-rpmvalidator
Summary:    Jolla Harbour RPM validation tools
Version:    1.2
Release:    1
Group:      System/Base
License:    GPLv2
BuildArch:  noarch
URL:        https://github.com/sailfishos/sdk-harbour-rpmvalidator
BuildRequires: python3-base
Requires:   binutils
Requires:   coreutils
Requires:   findutils
Requires:   sed
Requires:   cpio
Requires:   file
Requires:   grep
Source0:    %{name}-%{version}.tar.bz2

%description
RPM validation tools for Jolla Harbour.

%define debug_package %{nil}

%package sdk-tests
Summary: Verifies that the SDK really provides what %{name} promises
Group:   Development/Tools
Requires: %{name} = %{version}-%{release}
Requires: python3-base

# --auto-test-requires-BEGIN--
# Autogenerated by ./update-tests-requires.sh - do not edit manually
Requires: qml(Nemo.Configuration)
Requires: qml(Nemo.DBus)
Requires: qml(Nemo.Notifications)
Requires: qml(Nemo.Thumbnailer)
Requires: qml(QtGraphicalEffects)
Requires: qml(QtMultimedia)
Requires: qml(QtPositioning)
Requires: qml(QtQml)
Requires: qml(QtQml.Models)
Requires: qml(QtQuick)
Requires: qml(QtQuick.Layouts)
Requires: qml(QtQuick.LocalStorage)
Requires: qml(QtQuick.Particles)
Requires: qml(QtQuick.Window)
Requires: qml(QtQuick.XmlListModel)
Requires: qml(QtSensors)
Requires: qml(QtWebKit)
Requires: qml(Sailfish.Pickers)
Requires: qml(Sailfish.Silica)
Requires: qml(io.thp.pyotherside)
Requires: qml(org.freedesktop.contextkit)
# --auto-test-requires-END--

%description sdk-tests
%{summary}.

%prep
%setup -q

%build
./sdk-tests/check-qml-typeinfo.py -a allowed_qmlimports.conf \
                                  -d sdk-tests/deprecated_qmlimports.conf \
                                  create-tests-xml > sdk-tests/tests.xml

%install
rm -rf %{buildroot}

install -D -m 0755 rpmvalidation.sh %{buildroot}%{_bindir}/rpmvalidation.sh
install -D -m 0644 allowed_libraries.conf %{buildroot}%{_datadir}/%{name}/allowed_libraries.conf
install -D -m 0644 allowed_qmlimports.conf %{buildroot}%{_datadir}/%{name}/allowed_qmlimports.conf
install -D -m 0644 allowed_requires.conf %{buildroot}%{_datadir}/%{name}/allowed_requires.conf
install -D -m 0644 disallowed_qmlimport_patterns.conf %{buildroot}%{_datadir}/%{name}/disallowed_qmlimport_patterns.conf
install -D -m 0644 rpmvalidation.conf %{buildroot}%{_datadir}/%{name}/rpmvalidation.conf

# create version information file that is read by the validation script
echo "%{version}-%{release}" > %{buildroot}%{_datadir}/%{name}/version

install -D -m 0755 sdk-tests/check-qml-typeinfo.py %{buildroot}/opt/tests/%{name}/check-qml-typeinfo.py
install -D -m 0644 sdk-tests/deprecated_qmlimports.conf %{buildroot}/opt/tests/%{name}/deprecated_qmlimports.conf
install -D -m 0644 sdk-tests/tests.xml %{buildroot}/opt/tests/%{name}/tests.xml

%files
%defattr(-,root,root,-)
%{_bindir}/rpmvalidation.sh
%{_datadir}/%{name}/version
%{_datadir}/%{name}/*.conf

%files sdk-tests
%defattr(-,root,root,-)
/opt/tests/%{name}/*
