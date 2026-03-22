import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['node-red'])
@cli.command()
def deploy(): click.echo('Node-RED deployed')
if __name__ == '__main__': cli()
