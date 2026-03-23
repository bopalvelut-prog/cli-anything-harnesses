import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kairosdb running')
@cli.command()
def start(): click.echo('kairosdb started')
if __name__ == '__main__': cli()
