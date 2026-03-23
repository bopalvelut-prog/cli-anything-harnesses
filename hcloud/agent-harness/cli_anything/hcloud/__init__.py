import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hcloud running')
@cli.command()
def start(): click.echo('hcloud started')
if __name__ == '__main__': cli()
