import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prometheus_push running')
@cli.command()
def start(): click.echo('prometheus_push started')
if __name__ == '__main__': cli()
