if (( $# != 1 ))
then
  echo "Please supply figure name as first argument."
  exit 1
fi
figname=$1
curr_dir="$(dirname "$(realpath "$0")")"
cp "$curr_dir/template.tex" "./$figname.tex"
echo "created $figname.tex"
cp "$curr_dir/template.gp" "./$figname.gp"
echo "created $figname.gp"
