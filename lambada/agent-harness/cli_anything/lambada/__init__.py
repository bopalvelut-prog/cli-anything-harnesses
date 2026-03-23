import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lambada running')
@cli.command()
def start(): click.echo('lambada started')
if __name__ == '__main__': cli()
