import click
@click.group()
def cli(): pass
@cli.command()
def instances(): click.echo('EC2 instances')
@cli.command()
def start(): click.echo('EC2 start')
if __name__ == '__main__': cli()
