import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('abp running')
@cli.command()
def start(): click.echo('abp started')
if __name__ == '__main__': cli()
