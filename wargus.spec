Name:		wargus
Summary:	Warcraft II for the Stratagus game engine (Needs WC2 DOS CD)
Version:	3.0.0
Release:	1
Source0:	https://github.com/Wargus/wargus/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		http://wargus.sourceforge.net
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	stratagus-devel = %{version}

Requires:	ffmpeg2theora
Requires:	cdparanoia
Requires:	stratagus = %{version}
Recommends: ffmpeg

%description
Wargus is a Warcraft2 Mod that allows you to play Warcraft2 with the Stratagus
engine, as opposed to play it with the original Warcraft2 one. So unless you
have a legal copy of Warcraft2 (original DOS Version required, won't work with
the battle.net edition) Wargus will be pretty useless to you, since it doesn't
come with any graphics or sounds itself.

So why play Warcraft2 with the Stratagus engine instead of the original
Warcraft2 one? There are numerous reasons, first it allows you to play
Warcraft2 under GNU/Linux and other operating systems not supported by the
original Warcraft2 engine, secondly it allows you to play over the internet,
which the original Warcraft2 engine didn't allow you to. Last not least the
Stratagus engine allows you to tweak numerous parameters so you can play
around with different unit strength and such.

Since Wargus uses a different engine, not all things will work 100% the same
as they did in the original Warcraft2, if you want the original unchanged
Warcraft2 experience, you will still have to use the original Warcraft2.

Warcract2 game data should be installed to: /usr/share/games/stratagus/wargus/
Like: wartool -m -v -r [warcraft2_path]/data /usr/share/games/stratagus/wargus/

Warning! There are lots of hacked Warcraft2 versions that are NOT supported.
If you have problems with starting Wargus, most likely it's related to wrong
Warcraft2 data. Even if error messages are related to wrong/missing scripts.
The engine is tested and it does work.

%prep
%autosetup -p1

%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc README.md doc/*
%{_gamesbindir}/%{name}
%{_bindir}/wartool
%{_bindir}/pudconvert
%{_gamesdatadir}/stratagus/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Thu Sep 27 2012 Zombie Ryushu <ryushu@mandriva.org> 2.2.7-1mdv2012.0
+ Revision: 817687
- remove old patches
- Upgrade to 2.2.7

* Mon Jan 30 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.6-1
+ Revision: 769857
- Add patch0 and patch1 to fix build in Cooker (DSO and png issues)
- imported package wargus

