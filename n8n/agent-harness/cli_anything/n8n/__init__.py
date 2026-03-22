import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['n8n', 'start'])
@cli.command()
def list(): click.echo('n8n workflows')
if __name__ == '__main__': cli()
