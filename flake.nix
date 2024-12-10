{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};

    python = pkgs.python311;
  in {
    devShells.${system}.default = pkgs.mkShell {
      venvDir = "./venv";
      packages = with pkgs; [
        python

        pkgs.python311Packages.venvShellHook

        python.pkgs.icecream
      ];
    };
  };
}
