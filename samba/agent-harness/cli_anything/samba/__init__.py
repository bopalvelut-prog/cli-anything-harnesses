import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def shares(): click.echo('SMB shares')
@cli.command()
def status(): subprocess.run(['smbstatus'])
@cli.command()
def restart(): subprocess.run(['systemctl', 'restart', 'smbd'])
if __name__ == '__main__': cli()
