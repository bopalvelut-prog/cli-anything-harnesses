import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bagel running')
@cli.command()
def start(): click.echo('bagel started')
if __name__ == '__main__': cli()
