%define luaver 5.1
%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.1/resty

Name: luajit
Summary: OpenResty's Branch of LuaJIT 2
Version: 2.1.20220411
Release: 1%{?dist}
URL: https://github.com/yoannguion/luajit2
License: BSD
%if (0%{?rhel} == 7)
BuildRequires:	lua >= %{luaver}, lua-devel >= %{luaver}
Requires:	lua >= %{luaver}
%endif
%if (0%{?rhel} >= 8)
BuildRequires:	compat-lua >= %{luaver}, compat-lua-devel >= %{luaver}
Requires:	compat-lua >= %{luaver}
%endif

%description
OpenResty's Branch of LuaJIT 2


%build
cd %{_sourcedir}
make

%install
cd %{_sourcedir}
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT" PREFIX="/usr" MULTILIB="lib64"


%files
/usr/bin/luajit
/usr/bin/luajit-2.1.0-beta3
/usr/include/luajit-2.1/lauxlib.h
/usr/include/luajit-2.1/lua.h
/usr/include/luajit-2.1/lua.hpp
/usr/include/luajit-2.1/luaconf.h
/usr/include/luajit-2.1/luajit.h
/usr/include/luajit-2.1/lualib.h
/usr/lib64/libluajit-5.1.a
/usr/lib64/libluajit-5.1.so
/usr/lib64/libluajit-5.1.so.2
/usr/lib64/libluajit-5.1.so.2.1.0
/usr/share/luajit-2.1.0-beta3/jit/bc.lua
/usr/share/luajit-2.1.0-beta3/jit/bcsave.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_arm.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_arm64.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_arm64be.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_mips.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_mips64.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_mips64el.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_mipsel.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_ppc.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_x64.lua
/usr/share/luajit-2.1.0-beta3/jit/dis_x86.lua
/usr/share/luajit-2.1.0-beta3/jit/dump.lua
/usr/share/luajit-2.1.0-beta3/jit/p.lua
/usr/share/luajit-2.1.0-beta3/jit/v.lua
/usr/share/luajit-2.1.0-beta3/jit/vmdef.lua
/usr/share/luajit-2.1.0-beta3/jit/zone.lua


%changelog
* Thu Aug 04 2022 Yoann GUION <yoann.guion@gmail.com> -  2.1.20220411-1
- Initial release  2.1-20220411
