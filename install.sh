ln -s git.sh ~/git.sh
ln -s initsh.sh ~/.initsh
ln -s tmux.conf ~/.tmux.conf
ln -s vim ~/.vim
ln -s vimrc ~/.vimrc

sed -i -e "\$asource ~/.initsh" ~/.zshrc
