import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): subprocess.run(['fail2ban-client', 'status'])
@cli.command()
@click.argument('jail')
def unban(jail): subprocess.run(['fail2ban-client', 'set', jail, 'unbanip', 'all'])
@cli.command()
def restart(): subprocess.run(['systemctl', 'restart', 'fail2ban'])
if __name__ == '__main__': cli()
