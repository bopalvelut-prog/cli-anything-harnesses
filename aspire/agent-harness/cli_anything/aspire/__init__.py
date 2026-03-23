import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aspire running')
@cli.command()
def start(): click.echo('aspire started')
if __name__ == '__main__': cli()
