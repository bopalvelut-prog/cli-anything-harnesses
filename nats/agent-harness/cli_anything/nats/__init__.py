import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def subscribe(): click.echo('NATS subscribe')
@cli.command()
@click.argument('subject')
@click.argument('message')
def publish(subject, message): click.echo(f'Published to {subject}')
@cli.command()
def status(): click.echo('NATS server status')
if __name__ == '__main__': cli()
