import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jetty running')
@cli.command()
def start(): click.echo('jetty started')
if __name__ == '__main__': cli()
