Name     : wlr-randr
Version  : 0.4.1
Release  : 1
URL      : https://git.sr.ht/~emersion/wlr-randr
Source0  : https://git.sr.ht/~emersion/wlr-randr/archive/v%{version}.tar.gz
Summary  : Dynamic display configuration
Group    : Development/Tools
License  : MIT
BuildRequires : cmake
BuildRequires : buildreq-meson
BuildRequires : wayland-dev wayland-protocols-dev

%description
wlr-randr is a command line utility to manage outputs of a Wayland compositor.

%prep
%setup -q -n wlr-randr-v%{version}

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wlr-randr
