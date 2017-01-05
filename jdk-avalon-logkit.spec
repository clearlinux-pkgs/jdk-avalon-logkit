Name     : jdk-avalon-logkit
Version  : 2.1
Release  : 1
URL      : http://repo.maven.apache.org/maven2/avalon-logkit/avalon-logkit/2.1/avalon-logkit-2.1.jar
Source0  : http://repo.maven.apache.org/maven2/avalon-logkit/avalon-logkit/2.1/avalon-logkit-2.1.jar
Source1  : http://repo.maven.apache.org/maven2/avalon-logkit/avalon-logkit/2.1/avalon-logkit-2.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-avalon-logkit-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-avalon-logkit package.
Group: Data

%description data
data components for the jdk-avalon-logkit package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/avalon-logkit.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/avalon-logkit.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/avalon-logkit.xml \
%{buildroot}/usr/share/maven-poms/avalon-logkit.pom \
%{buildroot}/usr/share/java/avalon-logkit.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/avalon-logkit.jar
/usr/share/maven-metadata/avalon-logkit.xml
/usr/share/maven-poms/avalon-logkit.pom
