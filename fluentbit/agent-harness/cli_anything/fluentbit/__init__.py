import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fluentbit running')
@cli.command()
def start(): click.echo('fluentbit started')
if __name__ == '__main__': cli()
