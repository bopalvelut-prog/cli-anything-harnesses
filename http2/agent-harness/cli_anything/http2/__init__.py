import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('http2 running')
@cli.command()
def start(): click.echo('http2 started')
if __name__ == '__main__': cli()
