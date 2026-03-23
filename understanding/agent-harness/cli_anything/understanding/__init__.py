import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('understanding running')
@cli.command()
def start(): click.echo('understanding started')
if __name__ == '__main__': cli()
