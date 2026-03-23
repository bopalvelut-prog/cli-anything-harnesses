import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wolf running')
@cli.command()
def start(): click.echo('wolf started')
if __name__ == '__main__': cli()
