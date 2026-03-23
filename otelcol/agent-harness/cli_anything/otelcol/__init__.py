import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('otelcol running')
@cli.command()
def start(): click.echo('otelcol started')
if __name__ == '__main__': cli()
