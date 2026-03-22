import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def console(): subprocess.run(['msfconsole'])
@cli.command()
def db_status(): subprocess.run(['msfdb', 'status'])
@cli.command()
def version(): subprocess.run(['msfconsole', '-v'])
if __name__ == '__main__': cli()
