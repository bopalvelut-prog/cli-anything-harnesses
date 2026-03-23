import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strict running')
@cli.command()
def start(): click.echo('strict started')
if __name__ == '__main__': cli()
