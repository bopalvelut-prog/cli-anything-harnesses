import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['vercel', 'dev'])
@cli.command()
def deploy(): subprocess.run(['vercel', 'deploy'])
@cli.command()
def list(): subprocess.run(['vercel', 'ls'])
if __name__ == '__main__': cli()
