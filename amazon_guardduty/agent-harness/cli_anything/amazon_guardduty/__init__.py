import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_guardduty running')
@cli.command()
def start(): click.echo('amazon_guardduty started')
if __name__ == '__main__': cli()
