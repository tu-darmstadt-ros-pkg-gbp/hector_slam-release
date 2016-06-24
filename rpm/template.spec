Name:           ros-jade-hector-map-tools
Version:        0.3.5
Release:        0%{?dist}
Summary:        ROS hector_map_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_map_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-nav-msgs
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-nav-msgs

%description
hector_map_tools contains some functions related to accessing information from
OccupancyGridMap maps. Currently consists of a single header.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Jun 24 2016 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.5-0
- Autogenerated by Bloom

* Sat Nov 07 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom

