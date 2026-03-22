import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vsftpd running on :21')
@cli.command()
def restart(): subprocess.run(['systemctl', 'restart', 'vsftpd'])
if __name__ == '__main__': cli()
