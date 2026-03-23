import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dialyzer running')
@cli.command()
def start(): click.echo('dialyzer started')
if __name__ == '__main__': cli()
