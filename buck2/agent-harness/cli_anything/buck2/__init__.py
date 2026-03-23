import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buck2 running')
@cli.command()
def start(): click.echo('buck2 started')
if __name__ == '__main__': cli()
