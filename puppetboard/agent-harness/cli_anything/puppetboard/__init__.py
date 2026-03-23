import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('puppetboard running')
@cli.command()
def start(): click.echo('puppetboard started')
if __name__ == '__main__': cli()
