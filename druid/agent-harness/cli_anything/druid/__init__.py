import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('druid running')
@cli.command()
def start(): click.echo('druid started')
if __name__ == '__main__': cli()
