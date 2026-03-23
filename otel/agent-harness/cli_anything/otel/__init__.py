import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('otel running')
@cli.command()
def start(): click.echo('otel started')
if __name__ == '__main__': cli()
