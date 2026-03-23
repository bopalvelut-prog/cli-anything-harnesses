import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('treat running')
@cli.command()
def start(): click.echo('treat started')
if __name__ == '__main__': cli()
