import click
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Azure VM list')
@cli.command()
def start(): click.echo('Azure VM start')
if __name__ == '__main__': cli()
