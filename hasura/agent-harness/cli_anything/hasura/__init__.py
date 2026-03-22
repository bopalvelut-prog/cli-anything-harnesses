import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def console(): subprocess.run(['hasura', 'console'])
@cli.command()
def migrate(): subprocess.run(['hasura', 'migrate', 'apply'])
if __name__ == '__main__': cli()
