import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('detail running')
@cli.command()
def start(): click.echo('detail started')
if __name__ == '__main__': cli()
