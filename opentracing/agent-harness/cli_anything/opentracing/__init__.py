import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('opentracing running')
@cli.command()
def start(): click.echo('opentracing started')
if __name__ == '__main__': cli()
