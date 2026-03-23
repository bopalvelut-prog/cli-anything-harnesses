import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lonely running')
@cli.command()
def start(): click.echo('lonely started')
if __name__ == '__main__': cli()
