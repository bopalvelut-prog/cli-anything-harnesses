import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clinic running')
@cli.command()
def start(): click.echo('clinic started')
if __name__ == '__main__': cli()
