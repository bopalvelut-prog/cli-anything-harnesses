import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('listen running')
@cli.command()
def start(): click.echo('listen started')
if __name__ == '__main__': cli()
