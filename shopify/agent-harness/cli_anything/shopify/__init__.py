import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['shopify', 'app', 'dev'])
@cli.command()
def deploy(): subprocess.run(['shopify', 'app', 'deploy'])
if __name__ == '__main__': cli()
