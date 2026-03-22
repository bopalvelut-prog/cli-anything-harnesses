import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): subprocess.run(['prisma', 'migrate', 'dev'])
@cli.command()
def studio(): subprocess.run(['prisma', 'studio'])
if __name__ == '__main__': cli()
